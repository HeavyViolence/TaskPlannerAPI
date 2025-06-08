from model.configs.id_factory_config_loader import IDFactoryConfigLoader
from model.id.alphanumeric_id import AlphanumericID
from model.id.custom_id import CustomID
from model.id.id_type import IDType
from model.id.integer_id import IntegerID
from model.id.time_sortable_id import TimeSortableID

class IDFactory:
    def __init__(self, config_loader: IDFactoryConfigLoader):
        self._config: dict = config_loader.load()

    @property
    def config(self) -> dict:
        return self._config

    def create(self) -> CustomID:
        match self._config['id_type']:
            case IDType.TIME_SORTABLE.value:
                return TimeSortableID(self._config['byte_length'])
            case IDType.ALPHANUMERIC.value:
                return AlphanumericID(self._config['byte_length'])
            case IDType.INTEGER.value:
                return IntegerID(self._config['byte_length'])
            case _:
                return TimeSortableID(self._config['byte_length'])