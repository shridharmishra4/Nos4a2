import datetime

import numpy as np

from bson.objectid import ObjectId
from keras.callbacks import Callback

# todo: standardize class mapping
# todo: send class mapping to metrics


class TrainingStatusGenerator(Callback):
    def __init__(self, model_name, fold, num_folds, status_writers=[], final_round=True, total_epochs=np.inf):
        super().__init__()
        self.status_writers = status_writers
        self.model_base_status = {
            "ModelName": model_name,
            "FinalRound": final_round,
            "CurrentFold": fold + 1,
            "NumFolds": num_folds,
            "TotalEpochs": total_epochs,
            "Status": "Incomplete"
        }

    def on_epoch_end(self, epoch, logs=None):
        current_status = {
            "TrainLoss": logs.get('loss'),
            "TrainAccuracy": logs.get('acc'),
            "Epoch": epoch + 1,
            "Time": datetime.datetime.now()

        }

        if self.model_base_status['NumFolds'] > 1 or self.model_base_status['FinalRound']:
            current_status['ValidationLoss'] = logs.get('val_loss')
            current_status['ValidationAccuracy'] = logs.get('val_acc')

        for status_writer in self.status_writers:
            status_writer.write_one_status(self.model_base_status, current_status)

    def on_train_end(self, logs=None):
        search_filter = {}
        posts = self.status_writers[0].read_status(self.model_base_status)
        if posts.count() == 1:
            for post in posts:
                current_status = post.copy()
                current_status["Status"] = 'Complete'
                current_status['TotalEpochs'] = current_status['Epoch'] + 1
                current_status['Time'] = datetime.datetime.now()
                if self.model_base_status['NumFolds'] == 1:
                    base_status = self.model_base_status.copy()
                    base_status["FinalRound"] = not base_status['FinalRound']
                    base_status['Epoch'] = current_status['Epoch']
                    old_posts = self.status_writers[0].read_status(base_status)
                    if old_posts.count() == 1:
                        for old_post in old_posts:
                            current_status['ValidationLoss'] = old_post['ValidationLoss']
                            current_status['ValidationAccuracy'] = old_post['ValidationAccuracy']
                search_filter = {'_id': ObjectId(post['_id'])}

            for status_writer in self.status_writers:
                status_writer.write_end_status(search_filter, current_status)