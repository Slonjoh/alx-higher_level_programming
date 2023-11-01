#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object.
 * @p: A PyObject pointer representing the Python string.
 *
 * This function takes a PyObject pointer and checks if it is a valid Python
 * string object.
 */

void print_python_string(PyObject *p)
{
	const char *type = "compact unicode object";

	if (PyUnicode_Check(p))
	{
		Py_UNICODE *value = PyUnicode_AsUnicode(p);
		Py_ssize_t length = PyUnicode_GET_LENGTH(p);

		if (PyUnicode_IS_COMPACT_ASCII(p))
		{
			type = "compact ascii";
		}

		printf("[.] string object info\n");
		printf("  type: %s\n", type);
		printf("  length: %ld\n", length);
		printf("  value: %ls\n", value);
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
/**
 * main - Runs code
 * Return: 0
 */

int main(void)
{
	Py_Initialize();

	Py_Finalize();

	return (0);
}
