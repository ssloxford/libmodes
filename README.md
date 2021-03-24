# libmodes

This project is a development of @watson's [libmodes](https://github.com/watson/libmodes), which was itself a refactoring of the popular [dump1090](https://github.com/antirez/dump1090) project. This project continues the modularisation applied in [libmodes](https://github.com/watson/libmodes).

## Additions in this project fork

This version includes the following changes:

* Additional refactoring; breaking large detection routines into smaller functions, to make control flow clearer.
* Access provided to the intermediate detection and demodulation results:
```
	//structure capturing the results of processing a message, indicating how far the detection/demod got
	struct mode_s_detect_result {
		int preamble_found;
		int phase_corrected;
		int demod_error_count;
		int delta_test_result;
		int good_message;
		int msgtype;
		int msglen;
		struct mode_s_msg mm;
	};
	
	//one iteration of the internal loop in mode_s_detect, returning a detection result for that offset j
	void mode_s_detect_oneoffset(mode_s_t *self, struct mode_s_detect_result *result, uint16_t *mag, uint32_t maglen, uint32_t j)
	
	//find the first instance of a (potential) message in a given buffer of samples, returning the detection result and (if applicable) the message
	void mode_s_detectfirst(mode_s_t state, struct mode_s_detect_result *result, unsigned char *data, int data_len);
	
```
* All functionality is backwards compatible with the original libmodes.

A more detailed readme for the original libmodes library is available from the relevant Github page [here](https://github.com/watson/libmodes). All functionality is backwards compatible, so everything there should still work.

## License

BSD-2-Clause