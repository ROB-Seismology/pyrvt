#!/usr/bin/env python3
# encoding: utf-8

import os

from numpy.testing import assert_almost_equal, assert_allclose

import pyrvt.tests.readers as readers

class TestLoadFourierSpectrum:
    def __init__(self):
        self.d = readers.load_fourier_spectrum(
            os.path.join(
                os.path.dirname(__file__),
                'data',
                'test-bj84.m6.00r0020.0_fs.col'))

    def test_mag(self):
        assert_almost_equal(self.d['mag'], 6.00)

    def test_dist(self):
        assert_almost_equal(self.d['dist'], 20.00)

    def test_freq(self):
        assert_allclose(
            self.d['freqs'],
            [5.000E-02, 5.213E-02, 5.435E-02, 5.666E-02, 5.907E-02, 6.158E-02,
             6.421E-02, 6.694E-02, 6.979E-02, 7.276E-02, 7.585E-02, 7.908E-02,
             8.245E-02, 8.596E-02, 8.962E-02, 9.343E-02, 9.741E-02, 1.016E-01,
             1.059E-01, 1.104E-01, 1.151E-01, 1.200E-01, 1.251E-01, 1.304E-01,
             1.360E-01, 1.417E-01, 1.478E-01, 1.541E-01, 1.606E-01, 1.675E-01,
             1.746E-01, 1.820E-01, 1.898E-01, 1.978E-01, 2.063E-01, 2.150E-01,
             2.242E-01, 2.337E-01, 2.437E-01, 2.540E-01, 2.649E-01, 2.761E-01,
             2.879E-01, 3.001E-01, 3.129E-01, 3.262E-01, 3.401E-01, 3.546E-01,
             3.697E-01, 3.854E-01, 4.018E-01, 4.189E-01, 4.367E-01, 4.553E-01,
             4.747E-01, 4.949E-01, 5.160E-01, 5.379E-01, 5.608E-01, 5.847E-01,
             6.096E-01, 6.355E-01, 6.626E-01, 6.907E-01, 7.201E-01, 7.508E-01,
             7.828E-01, 8.161E-01, 8.508E-01, 8.870E-01, 9.248E-01, 9.641E-01,
             1.005E+00, 1.048E+00, 1.093E+00, 1.139E+00, 1.187E+00, 1.238E+00,
             1.291E+00, 1.346E+00, 1.403E+00, 1.463E+00, 1.525E+00, 1.590E+00,
             1.657E+00, 1.728E+00, 1.802E+00, 1.878E+00, 1.958E+00, 2.041E+00,
             2.128E+00, 2.219E+00, 2.313E+00, 2.412E+00, 2.514E+00, 2.621E+00,
             2.733E+00, 2.849E+00, 2.971E+00, 3.097E+00, 3.229E+00, 3.366E+00,
             3.510E+00, 3.659E+00, 3.815E+00, 3.977E+00, 4.146E+00, 4.323E+00,
             4.507E+00, 4.698E+00, 4.898E+00, 5.107E+00, 5.324E+00, 5.551E+00,
             5.787E+00, 6.033E+00, 6.290E+00, 6.558E+00, 6.837E+00, 7.128E+00,
             7.431E+00, 7.748E+00, 8.077E+00, 8.421E+00, 8.780E+00, 9.153E+00,
             9.543E+00, 9.949E+00, 1.037E+01, 1.081E+01, 1.127E+01, 1.175E+01,
             1.225E+01, 1.278E+01, 1.332E+01, 1.389E+01, 1.448E+01, 1.509E+01,
             1.574E+01, 1.641E+01, 1.710E+01, 1.783E+01, 1.859E+01, 1.938E+01,
             2.021E+01, 2.107E+01, 2.196E+01, 2.290E+01, 2.387E+01, 2.489E+01,
             2.595E+01, 2.705E+01, 2.820E+01, 2.940E+01, 3.065E+01, 3.196E+01,
             3.332E+01, 3.474E+01, 3.622E+01, 3.776E+01, 3.936E+01, 4.104E+01,
             4.279E+01, 4.461E+01, 4.651E+01, 4.848E+01, 5.055E+01, 5.270E+01,
             5.494E+01, 5.728E+01, 5.972E+01, 6.226E+01, 6.491E+01, 6.767E+01,
             7.055E+01, 7.355E+01, 7.669E+01, 7.995E+01, 8.335E+01, 8.690E+01,
             9.060E+01, 9.445E+01, 9.847E+01, 1.027E+02, 1.070E+02, 1.116E+02,
             1.163E+02, 1.213E+02, 1.265E+02, 1.318E+02, 1.374E+02, 1.433E+02,
             1.494E+02, 1.557E+02, 1.624E+02, 1.693E+02, 1.765E+02, 1.840E+02,
             1.918E+02, 2.000E+02])

    def test_fourier_amp(self):
        assert_allclose(
            self.d['fourier_amps'],
            [2.56424E-01, 2.78117E-01, 3.01592E-01, 3.26985E-01, 3.54442E-01,
             3.84116E-01, 4.16172E-01, 4.50783E-01, 4.88130E-01, 5.28404E-01,
             5.71807E-01, 6.18545E-01, 6.68836E-01, 7.22902E-01, 7.80972E-01,
             8.43277E-01, 9.10052E-01, 9.84194E-01, 1.06863E+00, 1.15950E+00,
             1.25715E+00, 1.36192E+00, 1.47413E+00, 1.59408E+00, 1.72203E+00,
             1.85821E+00, 2.00279E+00, 2.15588E+00, 2.31748E+00, 2.48753E+00,
             2.66582E+00, 2.85203E+00, 3.04566E+00, 3.24604E+00, 3.46270E+00,
             3.69178E+00, 3.92976E+00, 4.17620E+00, 4.43053E+00, 4.69210E+00,
             4.96015E+00, 5.23381E+00, 5.51212E+00, 5.79402E+00, 6.07841E+00,
             6.36406E+00, 6.64975E+00, 6.93418E+00, 7.21603E+00, 7.49399E+00,
             7.76673E+00, 8.03296E+00, 8.29143E+00, 8.54091E+00, 8.78027E+00,
             9.00841E+00, 9.22434E+00, 9.42713E+00, 9.61596E+00, 9.79006E+00,
             9.98162E+00, 1.02165E+01, 1.04433E+01, 1.06616E+01, 1.08714E+01,
             1.10725E+01, 1.12649E+01, 1.14484E+01, 1.16232E+01, 1.17892E+01,
             1.19465E+01, 1.20953E+01, 1.22505E+01, 1.25065E+01, 1.27580E+01,
             1.30048E+01, 1.32470E+01, 1.34845E+01, 1.37172E+01, 1.39450E+01,
             1.41679E+01, 1.43858E+01, 1.45985E+01, 1.48059E+01, 1.50080E+01,
             1.52046E+01, 1.53955E+01, 1.55805E+01, 1.57595E+01, 1.58762E+01,
             1.59276E+01, 1.59709E+01, 1.60058E+01, 1.60325E+01, 1.60506E+01,
             1.60601E+01, 1.60609E+01, 1.60527E+01, 1.60354E+01, 1.60089E+01,
             1.59729E+01, 1.59274E+01, 1.58721E+01, 1.58068E+01, 1.57313E+01,
             1.56455E+01, 1.55492E+01, 1.54423E+01, 1.53245E+01, 1.51958E+01,
             1.50559E+01, 1.49109E+01, 1.47604E+01, 1.45983E+01, 1.44243E+01,
             1.42385E+01, 1.40409E+01, 1.38314E+01, 1.36100E+01, 1.33769E+01,
             1.31322E+01, 1.28760E+01, 1.26085E+01, 1.23300E+01, 1.20407E+01,
             1.17410E+01, 1.14312E+01, 1.11118E+01, 1.06800E+01, 1.02332E+01,
             9.78692E+00, 9.34185E+00, 8.89861E+00, 8.45775E+00, 8.01979E+00,
             7.58515E+00, 7.15413E+00, 6.72692E+00, 6.30354E+00, 5.88381E+00,
             5.46741E+00, 5.05387E+00, 4.64264E+00, 4.23337E+00, 3.82605E+00,
             3.42155E+00, 3.02199E+00, 2.63111E+00, 2.25435E+00, 1.89843E+00,
             1.57033E+00, 1.27603E+00, 1.01941E+00, 8.01700E-01, 6.21608E-01,
             4.75914E-01, 3.60292E-01, 2.70019E-01, 2.00513E-01, 1.47632E-01,
             1.07818E-01, 7.81256E-02, 5.61734E-02, 4.00773E-02, 2.83701E-02,
             1.99226E-02, 1.38758E-02, 9.58275E-03, 6.56006E-03, 4.45014E-03,
             2.99040E-03, 1.98982E-03, 1.31055E-03, 8.54005E-04, 5.50358E-04,
             3.50595E-04, 2.20662E-04, 1.37149E-04, 8.41329E-05, 5.09105E-05,
             3.03716E-05, 1.78517E-05, 1.03318E-05, 5.88387E-06, 3.29494E-06,
             1.81309E-06, 9.79606E-07, 5.19287E-07, 2.69861E-07, 1.37364E-07,
             6.84278E-08, 3.33283E-08, 1.58562E-08, 7.36148E-09, 3.33157E-09,
             1.46819E-09, 6.29330E-10, 2.62070E-10, 1.05895E-10, 4.14649E-11])

class TestLoadRvtResponseSpectrum:
    def __init__(self):
        self.d = readers.load_rvt_response_spectrum(
            os.path.join(
                os.path.dirname(__file__),
                'data',
                'test-bj84.m6.00r020.0_rs.rv.col'))

    def test_mag(self):
        assert_almost_equal(self.d['mag'], 6.00)

    def test_dist(self):
        assert_almost_equal(self.d['dist'], 20.00)

    def test_damping(self):
        assert_almost_equal(self.d['damping'], 0.05)

    def test_duration(self):
        assert_allclose(self.d['duration'], 4.542)

    def test_freq(self):
        assert_allclose(
            self.d['freqs'],
            [25.000, 23.810, 22.727, 21.739, 20.833, 20.000, 18.182, 16.667,
             15.385, 14.286, 13.333, 12.500, 11.765, 11.111, 10.526, 10.000,
             9.091, 8.333, 7.692, 7.143, 6.667, 6.250, 5.882, 5.556, 5.263,
             5.000, 4.545, 4.167, 3.846, 3.571, 3.333, 3.125, 2.941, 2.778,
             2.632, 2.500, 2.381, 2.273, 2.174, 2.083, 2.000, 1.818, 1.667,
             1.538, 1.429, 1.333, 1.250, 1.176, 1.111, 1.053, 1.000, 0.909,
             0.833, 0.769, 0.714, 0.667, 0.625, 0.588, 0.556, 0.526, 0.500,
             0.455, 0.417, 0.385, 0.357, 0.333, 0.312, 0.294, 0.278, 0.263,
             0.250, 0.238, 0.227, 0.217, 0.208, 0.200, 0.182, 0.167, 0.154,
             0.143, 0.133, 0.125, 0.118, 0.111, 0.105, 0.100, 0.091, 0.083,
             0.077, 0.071, 0.067])

    def test_fourier_amp(self):
        assert_allclose(
            self.d['spec_accels'],
            [1.487E+02, 1.578E+02, 1.670E+02, 1.760E+02, 1.848E+02, 1.931E+02,
             2.117E+02, 2.274E+02, 2.405E+02, 2.514E+02, 2.606E+02, 2.683E+02,
             2.745E+02, 2.795E+02, 2.833E+02, 2.856E+02, 2.858E+02, 2.833E+02,
             2.794E+02, 2.747E+02, 2.695E+02, 2.639E+02, 2.582E+02, 2.524E+02,
             2.467E+02, 2.410E+02, 2.301E+02, 2.197E+02, 2.099E+02, 2.007E+02,
             1.920E+02, 1.839E+02, 1.762E+02, 1.691E+02, 1.623E+02, 1.560E+02,
             1.501E+02, 1.444E+02, 1.391E+02, 1.339E+02, 1.290E+02, 1.171E+02,
             1.065E+02, 9.731E+01, 8.924E+01, 8.214E+01, 7.584E+01, 7.024E+01,
             6.525E+01, 6.079E+01, 5.688E+01, 5.046E+01, 4.514E+01, 4.059E+01,
             3.664E+01, 3.318E+01, 3.017E+01, 2.757E+01, 2.532E+01, 2.331E+01,
             2.149E+01, 1.834E+01, 1.572E+01, 1.353E+01, 1.170E+01, 1.016E+01,
             8.865E+00, 7.771E+00, 6.844E+00, 6.055E+00, 5.382E+00, 4.806E+00,
             4.311E+00, 3.884E+00, 3.514E+00, 3.194E+00, 2.561E+00, 2.099E+00,
             1.752E+00, 1.486E+00, 1.279E+00, 1.115E+00, 9.823E-01, 8.738E-01,
             7.839E-01, 7.087E-01, 5.912E-01, 5.030E-01, 4.342E-01, 3.791E-01,
             3.342E-01])

