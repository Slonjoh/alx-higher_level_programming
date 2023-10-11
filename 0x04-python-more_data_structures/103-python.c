#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject pointer to the Python bytes object
 *
 * Return - 0
 */

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_GET_SIZE(p);
		char *data = PyBytes_AS_STRING(p);

		printf("  size: %ld\n", size);
		printf("  trying string: ");
		if (size > 10)
		{
			size = 10;
		}
		for (Py_ssize_t i = 0; i < size; i++)
		{
			printf("%02x", data[i] & 0xFF);
			if (i < size - 1)
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject pointer to the Python list
 *
 * Return - 0
 */
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: ", i);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
		else if (PyLong_Check(item))
		{
			printf("int\n");
		}
		else if (PyFloat_Check(item))
		{
			printf("float\n");
		}
		else if (PyTuple_Check(item))
			printf("tuple\n");
		else if (PyList_Check(item))
			printf("list\n");
		else if (PyUnicode_Check(item))
		{
			printf("str\n");
		}
		else
		{
			printf("Unknown\n");
		}
	}
}
