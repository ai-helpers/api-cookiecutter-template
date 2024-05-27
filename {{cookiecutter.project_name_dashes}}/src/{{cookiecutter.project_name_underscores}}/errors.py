class APIError(Exception):
   """
   Base class for  API service
   """
   pass

class APIModelNotFoundError(APIError):
   """
   Raised when the Machine Learning (ML) model file cannot be found
   """
   pass

class APIModelNotLoadableError(APIError):
   """
   Raised when the Machine Learning (ML) model cannot be loaded back into memory
   """
   pass

class APIExternalDataLoadModuleError(APIError):
   """
   Raised when there is an issue with the external data loader module
   """
   pass