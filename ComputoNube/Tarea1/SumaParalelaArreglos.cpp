/* 
SumaParalelaArreglos.cpp : Este archivo contiene la función "main".La ejecución del programa 
comienza y termina ahí.
*/

#include <iostream>
#include <omp.h>
#include <ctime> //Librería para medir el tiempo

#define N 1000
#define chunk 100
#define mostrar 10

//Línea utilizada para eliminar el prefijo 'std::' de las líneas de código
using namespace std;
unsigned t0, t1;

void imprimeArreglo(float* d);

int main()
{
    t0 = clock();
    
/*
# ifdef _OPENMP
    cout << "OMP disponible y funcionando" << "\n";
# endif
*/

    cout << "------------------------------------------------------------------\n";
    cout << "|              SUMANDO ARREGLOS EN PARALELO                       |\n";
    cout << "------------------------------------------------------------------\n\n";
    
    float a[N], b[N], c[N];
    int i;

    for (i = 0; i < N; i++)
    {
        a[i] = i * 10;
        b[i] = (i + 3) * 3.7;
    }

    int pedazos = chunk;

   #pragma omp parallel for \
    shared(a,b,c, pedazos) private(i) \
    schedule(static, pedazos)

    for (i = 0; i < N; i++)
        c[i] = a[i] + b[i];

    cout << "Imprimiendo los primeros " << mostrar << " valores del arreglo a: \n";
    cout << "------------------------------------------------------------------\n";
    imprimeArreglo(a);
    cout << "\n\nImprimiendo los primeros " << mostrar << " valores del arreglo b: \n";
    cout << "------------------------------------------------------------------\n";
    imprimeArreglo(b);
    cout << "\n\nImprimiendo los primeros " << mostrar << " valores del arreglo c, suma de arreglos a[] + b[]:\n";
    cout << "------------------------------------------------------------------\n";
    imprimeArreglo(c);

    t1 = clock();
    double time = (double(t1 - t0) / CLOCKS_PER_SEC);

    cout << "\n\nTiempo de ejecucion: " << time << "\nCantidad de elementos a manejar en los arreglos: "
         << N << "\nTamano de los pedazos de los arreglos para que cada hilo se encargue de estos: "
         << chunk << "\nCantidad de datos a imprimir: " << mostrar;
}

void imprimeArreglo(float* d) {
    for (int x = 0; x < mostrar; x++)
    {
        cout << d[x] << "\t";

    }
    cout << endl;
}

// Ejecutar programa: Ctrl + F5 o menú Depurar > Iniciar sin depurar
// Depurar programa: F5 o menú Depurar > Iniciar depuración