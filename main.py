from model.configs.id_factory_config_loader import IDFactoryConfigLoader
from model.id.id_factory import IDFactory


def main():
    id_factory = IDFactory(IDFactoryConfigLoader())
    for _ in range(10):
        print(id_factory.create())

if __name__ == "__main__":
    main()