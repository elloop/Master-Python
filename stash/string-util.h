/*
 * =====================================================================================
 *
 *       Filename:  string-util.h
 *
 *    Description: 	console print util
 *
 *        Version:  1.0
 *        Created:  2010年02月20日 23时46分32秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  elloop, elloop@foxmail.com
 *   Organization:  China 
 *
 * =====================================================================================
 */

#ifndef  STRING_UTIL_INC
#define  STRING_UTIL_INC

#include <iostream>
#define	pc(x) cout << "************************" << (x) << "*********************" << endl
#define	ps(x) cout << #x " = " << (x) << endl			//
#define	p(x)  cout << (x)			//
#define	pln(x)  cout << (x);cr;			//
#define	cr    cout << endl			//

#endif   /* ----- #ifndef STRING_UTIL_INC  ----- */
