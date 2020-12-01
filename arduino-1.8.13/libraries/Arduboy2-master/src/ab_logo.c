/**
 * @file ab_logo.c
 * \brief
 * The ARDUBOY logo bitmap.
 */

#include <avr/pgmspace.h>

#ifndef ARDUBOY_LOGO_CREATED
#define ARDUBOY_LOGO_CREATED

// arduboy_logo.png
// drawBitmap() format
// 88x16
const uint8_t arduboy_logo[] PROGMEM = {
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x55, 0x55, 0x01, 0xAA, 0xAA, 0xAA
};

// arduboy_logo.png
// drawCompressed() format
// 88x16
const uint8_t arduboy_logo_compressed[] PROGMEM = {
0x57, 0x0F, 0x9C, 0x53, 0x72, 0x75, 0x29, 0xE5, 0x9C, 0x92,
0xCE, 0x95, 0x52, 0xAD, 0x4E, 0x49, 0xE7, 0x08, 0x09, 0xED,
0x76, 0xBB, 0xDD, 0x2A, 0xAB, 0xAC, 0x55, 0x92, 0x90, 0xD0,
0x6E, 0xB7, 0xDB, 0xAD, 0xB2, 0xCA, 0x5A, 0x25, 0xF9, 0xF8,
0xF0, 0xC6, 0x47, 0x48, 0x28, 0x95, 0x54, 0x52, 0x49, 0x25,
0x9D, 0x3A, 0x95, 0x5A, 0x3A, 0x45, 0x2A, 0xB7, 0x29, 0xA7,
0xE4, 0x76, 0xBB, 0x55, 0x56, 0x59, 0xAB, 0x24, 0x9F, 0x5D,
0x5B, 0x65, 0xD7, 0xE9, 0xEC, 0x92, 0x29, 0x3B, 0xA1, 0x4E,
0xA7, 0xD3, 0xE9, 0x74, 0x9A, 0x8F, 0x8F, 0xEF, 0xED, 0x76,
0xBB, 0x55, 0x4E, 0xAE, 0x52, 0xAD, 0x9C, 0x9C, 0x4F, 0xE7,
0xED, 0x76, 0xBB, 0xDD, 0x2E, 0x95, 0x53, 0xD9, 0x25, 0xA5,
0x54, 0xD6, 0x2A, 0xAB, 0xEC, 0x76, 0xBB, 0x54, 0x4E, 0x65,
0x97, 0x94, 0x3A, 0x22, 0xA9, 0xA4, 0x92, 0x4A, 0x2A, 0xE9,
0x94, 0x4D, 0x2D, 0x9D, 0xA2, 0x94, 0xCA, 0x5A, 0x65, 0x95,
0xDD, 0x6E, 0x97, 0xCA, 0xA9, 0xEC, 0x12, 0x55, 0x69, 0x42,
0x7A
};

// arduboy_logo.png
// Sprites::drawSelfMasked() format
// 88x16
const uint8_t arduboy_logo_sprite[] PROGMEM = {
88, 16,
0xF0, 0xF8, 0x9C, 0x8E, 0x87, 0x83, 0x87, 0x8E, 0x9C, 0xF8,
0xF0, 0x00, 0x00, 0xFE, 0xFF, 0x03, 0x03, 0x03, 0x03, 0x03,
0x07, 0x0E, 0xFC, 0xF8, 0x00, 0x00, 0xFE, 0xFF, 0x03, 0x03,
0x03, 0x03, 0x03, 0x07, 0x0E, 0xFC, 0xF8, 0x00, 0x00, 0xFF,
0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF,
0x00, 0x00, 0xFE, 0xFF, 0x83, 0x83, 0x83, 0x83, 0x83, 0xC7,
0xEE, 0x7C, 0x38, 0x00, 0x00, 0xF8, 0xFC, 0x0E, 0x07, 0x03,
0x03, 0x03, 0x07, 0x0E, 0xFC, 0xF8, 0x00, 0x00, 0x3F, 0x7F,
0xE0, 0xC0, 0x80, 0x80, 0xC0, 0xE0, 0x7F, 0x3F, 0xFF, 0xFF,
0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0xFF, 0xFF, 0x00,
0x00, 0xFF, 0xFF, 0x0C, 0x0C, 0x0C, 0x0C, 0x1C, 0x3E, 0x77,
0xE3, 0xC1, 0x00, 0x00, 0x7F, 0xFF, 0xC0, 0xC0, 0xC0, 0xC0,
0xC0, 0xE0, 0x70, 0x3F, 0x1F, 0x00, 0x00, 0x1F, 0x3F, 0x70,
0xE0, 0xC0, 0xC0, 0xC0, 0xE0, 0x70, 0x3F, 0x1F, 0x00, 0x00,
0x7F, 0xFF, 0xC1, 0xC1, 0xC1, 0xC1, 0xC1, 0xE3, 0x77, 0x3E,
0x1C, 0x00, 0x00, 0x1F, 0x3F, 0x70, 0xE0, 0xC0, 0xC0, 0xC0,
0xE0, 0x70, 0x3F, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
0xFF, 0xFF, 0x01, 0x00, 0x00, 0x00
};

#endif
