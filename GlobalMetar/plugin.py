###
# Copyright (c) 2013, Keiran Smith
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import urllib2

class GlobalMetar(callbacks.Plugin):
    """Add the help for "@plugin help GlobalMetar" here
    This should describe *how* to use this plugin."""
    threaded = True

    def metar(self, irc, msg, args, icao):
        try:
            metarString = urllib2.urlopen("http://weather.noaa.gov/pub/data/observations/metar/stations/%s.TXT" % icao.upper())
            metarString = metarString.read()
            metarString = metarString.split("\n")
            irc.reply("%s" % (metarString[1]))
        except urllib2.HTTPError, e:
            if e.code == 404:
                irc.reply("ICAO not found")
            else:
                irc.reply("Unknown error %d occured" % e.code)

    metar = wrap(metar, ['somethingWithoutSpaces'])

    def aboutmetar(self, irc, msg, args):
        irc.reply("GlobalMetar (c) 2013 Keiran Smith, Data Supplied by NOAA plugin Licensed under BSD Style License")

    about = wrap(aboutmetar)

Class = GlobalMetar


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
