%module pylibmodes

%{
#define SWIG_FILE_WITH_INIT
#include "mode-s.h"
%}

void mode_s_init(mode_s_t *self);
void mode_s_compute_magnitude_vector(unsigned char *data, uint16_t *mag, uint32_t size);
void mode_s_detect(mode_s_t *self, uint16_t *mag, uint32_t maglen, mode_s_callback_t);
void mode_s_decode(mode_s_t *self, struct mode_s_msg *mm, unsigned char *msg);
void mode_s_detect_oneoffset(mode_s_t *self, struct mode_s_detect_result *result, uint16_t *mag, uint32_t maglen, uint32_t j);
