import  logging

class LogGen:
    @staticmethod
    def logger():
        logger = logging.getLogger(__name__)
        filehandle = logging.FileHandler("../Logs/generate.log")
        # filehandle = logging.FileHandler("../")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        filehandle.setFormatter(formatter)
        logger.addHandler(filehandle)
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        return logger