import numpy as np

def madhu_seager_two_layers(pressures, pressure_points, reference_point, alphas, betas):
    """
    Own implementation of the Madhusudhan-Seager temperature-pressure profile as described in Madhusudhan and Seager (2009), excluding the
    third(deepest) layer, which the authors propose must be absent in cooler atmospheres. I developed this function because it provides
    a better fit to the  spectra of temperate sub-Neptunes compared to the original three-layer model.
    """

    # Unpacking the input params
    p_0, p_1, p_2 = pressure_points
    p_set, t_set = reference_point
    a_0, a_1 = alphas
    b_0, b_1 = betas

    # Masking the two regions
    p2_mask = (pressures >= p_1)
    p1_mask = pressures < p_1

    # If P_set lies in the layer 2
    if p_set >= p_1:
        print("Caso p_set en layer 2")
        t_2 = t_set - (1/a_1 * (np.log(p_set) - np.log(p_2)))**(1/b_1)
        t_1 = t_2 + (1/a_1 * (np.log(p_1) - np.log(p_2)))**(1/b_1)
        t_0 = t_1 - (1/a_0 * (np.log(p_1) - np.log(p_0)))**(1/b_0)

    # If P_set lies in the layer 1
    elif p_set < p_1:
        print("Caso p_set en layer 1")
        t_0 = t_set - (1/a_0 * (np.log(p_set) - np.log(p_0)))**(1/b_0)
        t_1 = t_0 + (1/a_0 * (np.log(p_1) - np.log(p_0)))**(1/b_0)
        t_2 = t_1 - (1/a_1 * (np.log(p_1) - np.log(p_2)))**(1/b_1)

    # P_2 (deepest) layer profile
    p2_region = pressures[p2_mask]
    t2_region = t_2 + (1/a_1 * (np.log(p2_region) - np.log(p_2)))**(1/b_1)

    # P_1 (upper) layer profile
    p1_region = pressures[p1_mask]
    t1_region = t_0 + (1/a_0 * (np.log(p1_region) - np.log(p_0)))**(1/b_0)

    
    return {
        'region_1': {
            'ps': p1_region,
            'ts': t1_region
        },
        'region_2': {
            'ps': p2_region,
            'ts': t2_region
        },
        'p_set': p_set,
        'p_0': p_0,
        'p_1': p_1,
        'p_2': p_2,
        't_set': t_set,
        't_0': t_0,
        't_1': t_1,
        't_2': t_2,
    }