from abc import ABC, abstractmethod
from json import JSONDecodeError
from pathlib import Path
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError

import json


class ConfigLoader(ABC):
    _DIRECTORY_NAME: Path = Path(__file__).resolve().parent

    def __init__(self, validate_config: bool):
        self._validate_config = validate_config

    @property
    def validation_enabled(self) -> bool:
        return self._validate_config

    def _get_config_path(self) -> Path:
        return self._DIRECTORY_NAME / self.get_config_name_with_extension()

    def load(self):
        try:
            with open(self._get_config_path(), 'r') as config:
                data = json.load(config)
                if self.validation_enabled:
                    validate(data, self.get_config_schema())
                return data
        except FileNotFoundError as e:
            print(e)
        except JSONDecodeError as e:
            print(e)
        except SchemaError as e:
            print(e)
        except ValidationError as e:
            print(e)
        except Exception as e:
            print(e)
        return {}

    @abstractmethod
    def get_config_name_with_extension(self) -> str:
        pass

    @abstractmethod
    def get_config_schema(self) -> dict:
        pass