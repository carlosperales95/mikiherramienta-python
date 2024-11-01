import math
import speedtest

# This Python class performs internet speed tests for both upload and download speeds and converts the results from bytes to megabytes.
class InternetTest():
    def __init__(self, threads = 1):
        """
        The function initializes a Speedtest object with a specified number of threads for testing internet connection.
        
        :param threads: The `threads` parameter in the `__init__` method is used to specify the number of threads to be used for the speed test. This parameter allows you to control the concurrency of the speed test by running multiple threads simultaneously to measure the download and upload speeds. Increasing the number of threads can, defaults to 1 (optional)
        """
        self.TITLE = "Test de conexion a Internet"
        self.MSG_TEST_FINISHED = "Test finalizado!"
        self.engine = speedtest.Speedtest(secure=True)
        self.threads = threads

    def bytes_to_megabytes(self, bytes):
        """
        The function `bytes_to_megabytes` converts a given number of bytes to megabytes and returns the result with a unit of "Mbps".
        
        :param bytes: The `bytes_to_megabytes` function you provided converts a given number of bytes to megabytes. The `bytes` parameter represents the number of bytes that you want to convert to megabytes
        :return: the value of `megabytes` rounded to 3 decimal places, followed by the string "Mbps".
        """
        power = math.pow(1024, 2)
        megabytes = round(bytes / power, 3)
        return f"{megabytes} Mbps"

    def test_upload(self):
        """
        The function `test_upload` tests the upload speed using the `engine.upload` method with a specified number of threads.
        :return: The `upload` variable is being returned from the `test_upload` method.
        """
        print("\nTesteando velocidad de subida...")
        upload = self.engine.upload(threads=self.threads)
        print("Test de subida completado!")
        return upload
    
    def test_download(self):
        """
        The function `test_download` tests the download speed using the specified number of threads and returns the download result.
        :return: The `download` variable is being returned from the `test_download` method.
        """
        print("\nTesteando velocidad de bajada...")
        download = self.engine.download(threads=self.threads)
        print("Test de descarga completado!")
        return download

    def full_test(self):
        """
        The `full_test` function prints a title, performs upload and download tests, and then prints the test results in megabytes.
        """
        print(self.TITLE)
        upload = self.test_upload()
        download = self.test_download()

        print(f"\n{self.MSG_TEST_FINISHED}")
        print("Subida: ", self.bytes_to_megabytes(upload))
        print("Bajada: ", self.bytes_to_megabytes(download))