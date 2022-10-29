import os
PROJECT_NAME = 'GAL'
ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
LOG_PATH = os.path.join(ROOT_PATH, 'data', 'log')

VERSION = 5

DISTANCE_FUNCTION = 'angular'
EPSILON = 1e-06

RELEVANT_SUBSPACE_NUMBER = 5
SUBSPACE_REPLACEMENT_RATIO = 0.25
RESET_EXCLUSION_RD_FACTOR = True

RD_CUTOFF = None
DEFAULT_RD_PERCENTILE_CUTOFF = 0.1
RD_CUTOFF_WINDOW_SIZE = 5
RD_DERIVING_FACTOR = 0.5

EXCLUSION_RD_FACTOR = 4.
MIN_EXCLUSION_RD_FACTOR = 0.
EXCLUSION_RD_DEDUCTION_FACTOR = 0.25

VOTING_VERSION = 'weighted_average'	# average / weighted_average / lowest / majority
GRADE_ASSIGNMENT_METHOD = 'nearest_true_grade' # parent / nearest_true_grade / gaussian_mixture / oc / moc
OUTLIER_REMOVAL = False

MARGINALNESS_NEIGHBOURHOOD_SIZE = None
MARGINALNESS_RD_FACTOR = 1.
SPACIOUSNESS_NEIGHBOUR_NUMBER = 5

OUTLIER_DENSITY_CONDITION = '== 0'
OUTLIER_SPACIOUSNESS_CONDITION = '>= 0'
OUTLIER_NEAREST_TRUE_GRADE_CONDITION = '> RD * 3'

LABEL_SEARCHING_BOUNDARY_FACTOR = 2.0
LABEL_KNN = 5

DELTA_LINK_THRESHOLD = None
DELTA_LINK_THRESHOLD_FACTOR = 1.3
DELTA_LINK_THRESHOLD_WINDOW_SIZE_FACTOR = 0.1

DEBUG = False

# RANDOM_SEED = 3
RANDOM_SEED = 0
# RANDOM_SEED = None