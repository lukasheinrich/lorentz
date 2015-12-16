import ROOT
import array
import pickle

def main():
    ps = ROOT.TGenPhaseSpace()
    parent = ROOT.TLorentzVector()

    mass = 90.0
    parent.SetPtEtaPhiM(0,0,0,mass)
    
    childmasses = [0,0]
    ps.SetDecay(parent,len(childmasses),array.array('d',childmasses))

    nsamples = 1000

    samples = []
    for x in xrange(nsamples):
        ps.Generate()
        v0 = ps.GetDecay(0)
        v1 = ps.GetDecay(1)
        samples.append([v0,v1])

    pickle.dump(samples,open('roottlv.pickle','w'))
    
if __name__=='__main__':
    main()