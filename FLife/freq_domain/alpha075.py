import numpy as np
from scipy.special import gamma

class Alpha075(object):
    """Class for fatigue life estimation using frequency domain 
    method by Benasciutti and Tovo [1]. 

    References
    ----------
    [1] Denis Benasciutti and Robert Tovo. Rainflow cycle distribution and
        fatigue damage in Gaussian random loadings. Technical report, Department
        of Engineering, University of Ferrara, 2004
    [2] Janko Slavič, Matjaž Mršnik, Martin Česnik, Jaka Javh, Miha Boltežar. 
        Vibration Fatigue by Spectral Methods, From Structural Dynamics to Fatigue Damage
        – Theory and Experiments, ISBN: 9780128221907, Elsevier, 1st September 2020
    """
    def __init__(self, spectral_data):
        '''Get needed values from reference object.

        :param spectral_data:  Instance of object SpectralData
        '''                        
        self.spectral_data = spectral_data
    
    def get_life(self, C, k):
        """Calculate fatigue life with parameters C, k, as defined in [2].

        :param C: [int,float]
            Fatigue strength coefficient [MPa**k].
        :param k : [int,float]
            Fatigue strength exponent [/].
        :return T: float
            Estimated fatigue life in seconds.
        """
        m0 = self.spectral_data.moments[0]
        nu = self.spectral_data.nu
        a075 = self.spectral_data.m075 / np.sqrt(m0 * self.spectral_data.m150)

        dNB = nu * np.sqrt(2 * m0)**k * gamma(1.0 + k/2.0) / C
        D =  a075**2 * dNB
        T = 1.0 / D
        
        return T