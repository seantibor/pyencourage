# API Reference

Import the pyencourage module to access `pyencourage` in any Python application:

```python
import pyencourage
```

## pyencourage.get_encouragement()

Returns a random encouragement from the given category in the given language.

| Parameters | Types | Values | Default |
| ---------- | ----- | ------ | ------- |
| language   | str   | 'en' | 'en' |
| category   | str   | 'neutral', 'zen', 'positivity', 'advice', 'all' | 'neutral' |

Return type: str

If the `language` value provided is not available, a `LanguageNotFoundError` exception is raised.

If the `category` value provided is not available, a `CategoryNotFoundError` exception is raised.

## pyencourage.get_encouragements()

Returns a list of encouragements from the given category in the given language.

| Parameters | Types | Values | Default |
| ---------- | ----- | ------ | ------- |
| language   | str   | 'en' | 'en' |
| category   | str   | 'neutral', 'zen', 'positivity', 'advice', 'all' | 'neutral' |

Return type: list

If the `language` value provided is not available, a `LanguageNotFoundError` exception is raised.

If the `category` value provided is not available, a `CategoryNotFoundError` exception is raised.

## Supported languages

These are all the languages supported by pyencourage:

| Language   | Value | 
| ---------- | ----- | 
| English    | 'en'  | 

To add support for another language, please see the [contributing page](https://github.com/seantibor/pyencourage/blob/master/CONTRIBUTING.md).
