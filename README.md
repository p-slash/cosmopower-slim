This is the slim version of [CosmoPower](https://github.com/alessiospuriomancini/cosmopower) that requires only numpy and numba. Tensorflow dependencies are removed. Please cite the original work.

# Citation

If you use ``CosmoPower`` at any point in your work please cite its [release paper](https://arxiv.org/abs/2106.03846):

    @article{SpurioMancini2022,
             title={CosmoPower: emulating cosmological power spectra for accelerated Bayesian inference from next-generation surveys},
             volume={511},
             ISSN={1365-2966},
             url={http://dx.doi.org/10.1093/mnras/stac064},
             DOI={10.1093/mnras/stac064},
             number={2},
             journal={Monthly Notices of the Royal Astronomical Society},
             publisher={Oxford University Press (OUP)},
             author={Spurio Mancini, Alessio and Piras, Davide and Alsing, Justin and Joachimi, Benjamin and Hobson, Michael P},
             year={2022},
             month={Jan},
             pages={1771–1788}
             }

If you use a specific likelihood or trained model then in addition to the [release paper](https://arxiv.org/abs/2106.03846) please _also_ cite their relevant papers (always listed in the corresponding directory). If you use the custom activation function implemented in the code please also cite [Alsing et al.(2020)](https://doi.org/10.3847/1538-4365/ab917f).


# License

``CosmoPower`` is released under the GPL-3 license (see [LICENSE](https://github.com/alessiospuriomancini/cosmopower/blob/main/LICENSE)) subject to 
the non-commercial use condition (see [LICENSE_EXT](https://github.com/alessiospuriomancini/cosmopower/blob/main/LICENSE_EXT)).

    CosmoPower
    Copyright (C) 2021 A. Spurio Mancini & contributors
    
    This program is released under the GPL-3 license (see LICENSE), 
    subject to a non-commercial use condition (see LICENSE_EXT).
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
