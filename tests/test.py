import lorentz
import pickle
import functools
import random
import ROOT

def tlv2tuple(tlv):
    return tlv.T(), tlv.X(), tlv.Y(), tlv.Z()

def validate(fromlorentz,fromroot):
    try:
        epsilon = 1e-10
        assert abs((fromroot.Eta()-fromlorentz.eta)/fromlorentz.eta) < epsilon
        assert abs((fromroot.Phi()-fromlorentz.phi)/fromlorentz.phi) < epsilon
        assert abs((fromroot.Theta()-fromlorentz.theta)/fromlorentz.theta) < epsilon
        assert abs((fromroot.Mag2()-fromlorentz.s2())/fromlorentz.s2()) < epsilon
        assert abs((fromroot.Perp2()-fromlorentz.perp2())/fromlorentz.perp2()) < epsilon
    except:
        print fromlorentz.components()
        IPython.embed()
        raise AssertionError

def testvec(randomnumber,ntests):
    for i in xrange(ntests):
        t,x,y,z = [randomnumber() for x in range(4)]
        fromroot = ROOT.TLorentzVector(x,y,z,t)
        fromlorentz = lorentz.FourVector(t,x,y,z)
        validate(fromlorentz,fromroot)
        print '{}/{}'.format(i+1,ntests)

def testsum(randomnumber,nsum):
    for i in xrange(nsum):
        t1,x1,y1,z1 = [randomnumber() for x in range(4)]
        t2,x2,y2,z2 = [randomnumber() for x in range(4)]
        
        fromroot1 = ROOT.TLorentzVector(x1,y1,z1,t1)
        fromroot2 = ROOT.TLorentzVector(x2,y2,z2,t2)
        
        fromlorentz1 = lorentz.FourVector(t1,x1,y1,z1)
        fromlorentz2 = lorentz.FourVector(t2,x2,y2,z2)
        
        sumlorentz = fromlorentz1+fromlorentz2
        sumroot    = fromroot1+fromroot2
        
        validate(sumlorentz,sumroot)
        print '{}/{}'.format(i+1,nsum)

def main():
    nsamples = 10000
    randomnumber = functools.partial(random.uniform,-10000,10000)
    testvec(randomnumber,10000)
    testsum(randomnumber,10000)

if __name__ == '__main__':
    main()