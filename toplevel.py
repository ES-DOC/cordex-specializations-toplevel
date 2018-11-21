"""A top level model.

"""
# --------------------------------------------------------------------
# CONTACT: Set to top-level specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Sebastien Denvil (IPSL)'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Sebastien Denvil (IPSL)'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to top-level specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Sebastien Denvil (IPSL), Mark Greenslade (IPSL)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2018-12-01", "Sebastien Denvil (IPSL)",
        "Initialised"),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific top-level
# --------------------------------------------------------------------
DESCRIPTION = 'Model top level'

# --------------------------------------------------------------------
# KEY PROPERTIES: File name (without the .py suffix) containing key properties of the top level model.
# --------------------------------------------------------------------
KEY_PROPERTIES = 'toplevel_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = None

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the model
# --------------------------------------------------------------------
PROCESSES = [
    'toplevel_radiative_forcings',
    ]
