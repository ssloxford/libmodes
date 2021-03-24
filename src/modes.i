%module pylibmodes

%{
#define SWIG_FILE_WITH_INIT
#include "mode-s.h"
%}

%include "numpy.i"
%init %{
import_array();
%}

//%apply (uint16_t* IN_ARRAY1, uint32_t DIM1) {(int* seq, int n)};
//%apply (unsigned char* IN_ARRAY1, uint32_t DIM1) {(unsigned char* data, uint32_t data_len)};
%apply (unsigned char* IN_ARRAY1, int DIM1) {(unsigned char* data, int data_len)};

%include "mode-s.h"
