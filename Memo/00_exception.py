# https://hyperskill.org/learn/step/11680
print("""
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- BaseExceptionGroup
+-- Exception
     +-- StopIteration
     +-- StopAsyncIteration
     +-- ArithmeticError
          +-- FloatingPointError
          +-- OverflowError
          +-- ZeroDivisionError
     +-- AssertionError
     +-- AttributeError
     +-- BufferError
     +-- EOFError
     +-- ExceptionGroup [BaseExceptionGroup]
     +-- ImportError
          +-- ModuleNotFoundError
     +-- LookupError
          +-- IndexError
          +-- KeyError
     +-- MemoryError
     +-- NameError
          +-- UnboundLocalError
     +-- OSError
          +-- BlockingIOError
          +-- ChildProcessError
          +-- ConnectionError
               +-- BrokenPipeError
               +-- ConnectionAbortedError
               +-- ConnectionRefusedError
               +-- ConnectionResetError
          +-- FileExistsError
          +-- FileNotFoundError
          +-- InterruptedError
          +-- IsADirectoryError
          +-- NotADirectoryError
          +-- PermissionError
          +-- ProcessLookupError
          +-- TimeoutError
     +-- ReferenceError
     +-- RuntimeError
          +-- NotImplementedError
          +-- RecursionError
     +-- SyntaxError
          +-- IndentationError
               +-- TabError
     +-- SystemError
     +-- TypeError
     +-- ValueError
          +-- UnicodeError
               +-- UnicodeDecodeError
               +-- UnicodeEncodeError
               +-- UnicodeTranslateError
     +-- Warning
          +-- DeprecationWarning
          +-- EncodingWarning
          +-- PendingDeprecationWarning
          +-- RuntimeWarning
          +-- SyntaxWarning
          +-- UserWarning
          +-- FutureWarning
          +-- ImportWarning
          +-- UnicodeWarning
          +-- BytesWarning
          +-- ResourceWarning
""")


try:
     n1 = int(input())
     n2 = int(input())
     result = n1 / n2
except ZeroDivisionError:
     print("ZeroDivisionError")
except (ValueError, TypeError):
     print("Only integers are allowed")
except Exception:
     print("Exception")
except:
     print("Exception 2")
else:
     print(result)
finally:
     print("finally done")

# try:
#      result = n1 / n2
# except ZeroDivisionError:
#      print("ZeroDivisionError")
# except:
#      print("Exception, try again")
# else:
#      print(result)
# finally:
#      print("finally done")