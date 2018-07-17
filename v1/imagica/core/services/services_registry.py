from .properties_services import DataProperties, StatusWriterConfig, ValidationProperties
from .data_services import APIDataService, FolderDataService, DBDataService
from .writer_services import DBStatusWriter
from .validation_services import NormalValidationCreator, StratifiedFormatIdentifiedValidationCreator, \
    TimeBasedValidationCreator


class ServiceRegistry:
    def __init__(self):
        self.data_service = None
        self.validation_service = None
        self.writer_service = None
        self.data_properties = DataProperties()
        self.status_writer_config = StatusWriterConfig()
        self.validation_properties = ValidationProperties()

    def register(self):
        data_services = {
            "DB": DBDataService,
            "Folder": FolderDataService,
            "API": APIDataService
        }
        validation_services = {
            "Normal": NormalValidationCreator,
            "StratifiedCluster": StratifiedFormatIdentifiedValidationCreator,
            "Time": TimeBasedValidationCreator
        }

        writer_services = {
            "DB": DBStatusWriter
        }

        if self.validation_properties.validation_type in validation_services:
            self.validation_service = validation_services[self.validation_properties.validation_type]

        if self.data_properties.source_type in data_services:
            self.data_service = data_services[self.data_properties.source_type]

        if self.status_writer_config.writer_type in writer_services:
            self.writer_service = writer_services[self.status_writer_config.writer_type]
