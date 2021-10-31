/*  The functions in this file compute the broadening factors.
 *  The names of the functions start with "Fc" followed by
 *  the label of the corresponding reaction.
 */

#include"BroadeningFactors.h"

/*	Mechanism file: "TheSoot.mech"	*/

BFFunction gBroadening[33] = { Fc12, Fc14, Fc27, FcG07, FcG10, FcG12, FcG13, FcG14, FcG24, FcG37, FcG43, FcG44, FcG51, FcG54, FcG60, FcG75, FcG83, FcG104, FcG115, FcG129, FcG154, FcG155, FcG163, FcG164, FcG172, FcG173, FcG180, FcG183, FcR053, FcH09, FcB08, FcT23, FcOX01 };

#ifndef MECHANISM
#define MECHANISM ""
#endif

void TReaction::CheckBroadeningFactors( const char *mechName )
{
	char	*name = new char[strlen( MECHANISM ) + 6];
	sprintf( name, "/%s.pre", MECHANISM );
	if ( strstr( mechName, name ) == NULL ) {
		for ( int i = 0; i < 33; ++i ) {
			gBroadening[i] = FcErr;
		}
	}
}

Double FcErr( Double /*T*/ )
{
	fprintf( stderr, "#error: wrong broadening factors (%s) linked to program\n", MECHANISM );
	exit( 2 );

	return 0;
}

Double Fc12( Double T )
{
#line 36 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double Fc14( Double T )
{
#line 41 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double Fc27( Double T )
{
#line 67 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG07( Double T )
{
#line 110 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG10( Double T )
{
#line 117 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG12( Double T )
{
#line 126 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG13( Double T )
{
#line 131 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG14( Double T )
{
#line 139 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG24( Double T )
{
#line 155 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG37( Double T )
{
#line 176 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG43( Double T )
{
#line 189 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG44( Double T )
{
#line 194 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG51( Double T )
{
#line 211 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG54( Double T )
{
#line 219 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG60( Double T )
{
#line 231 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG75( Double T )
{
#line 255 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG83( Double T )
{
#line 267 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG104( Double T )
{
#line 301 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG115( Double T )
{
#line 328 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG129( Double T )
{
#line 363 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG154( Double T )
{
#line 413 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG155( Double T )
{
#line 420 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG163( Double T )
{
#line 441 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG164( Double T )
{
#line 449 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG172( Double T )
{
#line 473 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG173( Double T )
{
#line 482 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG180( Double T )
{
#line 509 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcG183( Double T )
{
#line 524 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcR053( Double T )
{
#line 672 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcH09( Double T )
{
#line 905 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcB08( Double T )
{
#line 992 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcT23( Double T )
{
#line 2005 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

Double FcOX01( Double T )
{
#line 2439 "TheSoot.mech"

	fprintf( stderr, "#error: no broadening function specified\n" );
	exit( 2 );

	return T;
}

