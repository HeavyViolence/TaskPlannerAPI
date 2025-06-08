from model.configs.config_loader import ConfigLoader


class IDFactoryConfigLoader(ConfigLoader):
    def __init__(self, validate_config: bool = True):
        super().__init__(validate_config)

    def get_config_name_with_extension(self) -> str:
        return 'id_factory_config.json'

    def get_config_schema(self) -> dict:
        return {
            'type': 'object',
            'properties': {
                'id_type': {
                    'type': 'string',
                    'enum': ['time-sortable', 'alphanumeric', 'integer'],
                    'default': 'time-sortable'
                },
                'byte_length': {
                    'type': 'integer',
                    'minimum': 8,
                    'maximum': 32,
                    'default': 12
                }
            },
            'required': ['id_type', 'byte_length'],
            'additionalProperties': False
        }