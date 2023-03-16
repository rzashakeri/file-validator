---
sidebar_position: 1
---

# file validator

In the [0.X.X](https://file-validator.github.io/docs/0.X.X/intro) version, each of the File Validats was a separate function but in this version they are all become a class

In the new version you can validate files based on extension, mime and size separately

## How Used?
### First Imported
You must first import `FileValidator` to use:
```python
from file_validator.validators import FileValidator
```


### Create Instance
At this point you should make an instance from the `FileValidator` class:
```python
file_validator = FileValidator(
    acceptable_extensions=[".png"],
    max_upload_file_size=1000000,
    acceptable_types=["image", "audio"],
    acceptable_mimes=["image/png"],
    file_path="path/to/file",
)
```

### File Validation Using The **python-magic** Library
If you want to perform validation operations by the `python-magic` Library, you should use the `python_magic()` method as follows:

```python
file_validator.python_magic()
```


### File Validation Using The **pure-magic** Library
If you want to perform validation operations by the `pure-magic` Library, you should use the `pure_magic()` method as follows:

```python
file_validator.pure_magic()
```

### File Validation Using The **mimetypes** Library
If you want to perform validation operations by the `mimetypes` Library, you should use the `mimetypes()` method as follows:

```python
file_validator.mimetypes()
```