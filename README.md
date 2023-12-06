# SimoPAI

SimoPAI is a Python library that simplifies the usage of the OpenAI models for everyday text generation tasks. This library is designed to provide a more user-friendly and structured interface, allowing developers to harness the power of openAI technologies without the complexities of managing raw JSON data.

## Features

- Object-oriented design for easy interaction with OpenAI API.
- Streamlined text generation with simplified methods.
- Simplified integration into Python projects.
- Enhance your applications with AI-driven text generation effortlessly.

## Getting Started

1. Install SimoPAI via pip:
```bash
pip install simopai
```

2. Initialize a SimoPAI object with your OpenAI API key:
```python
from simopai import SimoPAI

# Replace 'YOUR_OPENAI_API_KEY' with your actual API key
simo = SimoPAI(api_key="YOUR_OPENAI_API_KEY")
```

3. Generate text using the library's simplified interface:
```python
# Generate text based on a prompt
response = simo.generate_text(prompt="Translate the following English text to French: 'Hello, world!'")

# Print the generated text
print(response)
```

## Documentation

To access the full documentation and learn more about SimoPAI, please visit the [SimoPAI documentation](https://github.com/nachokhan/simopai).

## Contributing

Contributions to SimoPAI are welcome! If you have ideas for improvements or find any issues, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
