import numpy as np

def calculate_scores(analytic, creative, practical, social, introvert, naturalist):
    dimensions = {
        'تحلیلی': analytic,
        'خلاق': creative,
        'عملی': practical,
        'اجتماعی': social,
        'درون‌گرا': introvert,
        'طبیعت‌گرا': naturalist
    }
    
    results = {}
    for name, scores in dimensions.items():
        arr = np.array(scores)
        results[name] = {
            'sum': np.sum(arr), # https://numpy.org/ or https://www.w3schools.com/python/numpy/default.asp
            'mean': np.mean(arr),
            'std': np.std(arr), # انحراف
            'raw': arr.tolist()
        }
    return results

def find_dominant_type(results):
    sums = {name: data['sum'] for name, data in results.items()}
    max_sum = max(sums.values())
    dominant = [name for name, s in sums.items() if s == max_sum]
    return dominant, max_sum

def normalize_scores(results, min_possible=125, max_possible=500):
    normalized = {}
    for name, data in results.items():
        total = data['sum']
        percent = ((total - min_possible) / (max_possible - min_possible)) * 100
        normalized[name] = round(percent, 1)
    return normalized