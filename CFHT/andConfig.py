root.starGalaxyColumn = "starnotgal"
filters = ('u', 'g', 'r', 'i', 'z')
root.magColumnMap = dict([(f,f) for f in filters])
root.magErrorColumnMap = dict([(f, f + '_err') for f in filters])
root.indexFiles = ['templ-D1.index.fits',
                   'templ-D2.index.fits',
                   'templ-D3.index.fits',
                   'templ-D4.index.fits',
                   ]
