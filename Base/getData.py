import yaml,os


class GetData:

    @classmethod
    def get_yaml_data(cls,name):
        with open("./Data" + os.sep + name, "r",encoding="utf-8") as f:
            # yaml读取文件
            data = yaml.safe_load(f)

