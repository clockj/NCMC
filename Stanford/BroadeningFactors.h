#define MECHANISM "TheSoot"
#include "FlameMaster.h"

/*	Mechanism file: "TheSoot.mech"	*/

typedef Double (*BFFunction)(Double T);

/* prototypes */
Double Fc12( Double T );
Double Fc14( Double T );
Double Fc27( Double T );
Double FcG07( Double T );
Double FcG10( Double T );
Double FcG12( Double T );
Double FcG13( Double T );
Double FcG14( Double T );
Double FcG24( Double T );
Double FcG37( Double T );
Double FcG43( Double T );
Double FcG44( Double T );
Double FcG51( Double T );
Double FcG54( Double T );
Double FcG60( Double T );
Double FcG75( Double T );
Double FcG83( Double T );
Double FcG104( Double T );
Double FcG115( Double T );
Double FcG129( Double T );
Double FcG154( Double T );
Double FcG155( Double T );
Double FcG163( Double T );
Double FcG164( Double T );
Double FcG172( Double T );
Double FcG173( Double T );
Double FcG180( Double T );
Double FcG183( Double T );
Double FcR053( Double T );
Double FcH09( Double T );
Double FcB08( Double T );
Double FcT23( Double T );
Double FcOX01( Double T );
Double FcErr( Double T );


extern BFFunction gBroadening[33];
