#include <Python.h>
#include <sys/types.h>
#include <pyport.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints size and allocation of list
 * @p: PyObject struct pointer
 * Return: No Value
 */
void print_python_list(PyObject *p)
{
	unsigned int psize = (unsigned int)(((PyVarObject *)(p))->ob_size), i;
	unsigned int pall = (unsigned int)(((PyListObject *)(p))->allocated);
	PyObject **plitem = ((PyListObject *)(p))->ob_item;
	char *pltype = (char *)((PyListObject *)(p)->ob_type->tp_name);
	char *ptype = NULL;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (p && !strcmp("list", pltype))
	{
		printf("[*] Size of the Python List = %u\n", psize);
		printf("[*] Allocated = %u\n", pall);
		for (i = 0; i < psize; i++)
		{
			ptype = (char *)(plitem[i])->ob_type->tp_name;
			printf("Element %d: %s\n", i, ptype);
			if (!strcmp("bytes", ptype))
				print_python_bytes(plitem[i]);
			else if (!strcmp("float", ptype))
				print_python_float(plitem[i]);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_bytes - prints size of bytes, string, and first few bytes
 * @p: PyObject struct pointer
 * Return: No Value
 */
void print_python_bytes(PyObject *p)
{
	unsigned int psize, i;
	char *ptype = NULL;

	setbuf(stdout, NULL);
	ptype = (char *)(p->ob_type->tp_name);
	printf("[.] bytes object info\n");
	if (p && !strcmp("bytes", ptype))
	{
		psize = (int)PyBytes_Size(p);
		printf("  size: %d\n", psize);
		printf("  trying string: %s\n", ((PyBytesObject *)(p))->ob_sval);
		if (psize < 10)
			printf("  first %d bytes: ", (psize + 1));
		else
			printf("  first 10 bytes: ");
		for (i = 0; i < psize + 1 && i < 10; i++)
		{
			printf("%02x",  (unsigned char)(((PyBytesObject *)(p))->ob_sval[i]));
			if ((i != psize) && (i < 9))
				printf(" ");
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_float - prints value of float
 * @p: PyObject struct pointer
 * Return: No Value
 */
void print_python_float(PyObject *p)
{
	char *pftype = (char *)((PyListObject *)(p)->ob_type->tp_name);
	double pdub = 0.0;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (p && !strcmp("float", pftype))
	{
		pdub = PyFloat_AsDouble(p);
		if (trunc(fmod((pdub * 10), 10)) != 0 || trunc(fmod((pdub / 10), 10)) != 0)
			printf("  value: %.17g\n", pdub);
		else
			printf("  value: %#.2g\n", pdub);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}
