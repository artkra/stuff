#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Plot Tupper's self-referential formula
"""

#N = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719
N = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300
H = 17
W = 1

import sys
if __name__ == '__main__':
    if len(sys.argv)>1: H = int(sys.argv[1])
    def tupper(x,y):
        return 0.5 < ((y//H) // (2**(H*x + y%H))) % 2

    print "x range: 0 < x <",
    W = int(raw_input())
    print 'Got width: %d' % W
    print "y range: N < y < N+%d, where N = (type 0 for default)" % H,
    t = int(raw_input())
    if t: N=t
    print

    import matplotlib.pyplot as plot
    plot.rc('patch', antialiased=False)
    print 'Plotting...'
    for x in xrange(W):
        print 'Column %d...' % x
        for yy in xrange(H):
            y = N + yy
            if tupper(x,y):
                plot.bar(left=x, bottom=yy, height=1, width=1, linewidth=0, color='black')
    print 'Done plotting, please wait...'

    plot.axis('scaled')
    #For large graphs, must change these values (smaller font size, wider-apart ticks)
    buf = 2
    plot.xlim((-buf,W+buf))
    plot.ylim((-buf,H+buf))
    plot.rc('font', size=10)
    plot.xticks(range(0, W, 100))
    yticks = range(0, H+1, 4)
    plot.yticks(yticks, ['N']+['N + %d'%i for i in yticks][1:])
    plot.savefig('out.png')
    plot.savefig('out.svg')
