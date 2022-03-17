from data_analysis import calc_fulfillment_of_demand, calc_mean_and_std_of_fullfillment, calc_average_pressure, \
    five_node_tuple
from data_loading import load_data, check_plausibility
from plotting import plot_fullfillment

# exercise 1 a)
# radius = "Radius_500"
# center_node = "Center_node_J1025"
# rescue_node = "Rescue_node_J1223"
radius = "Radius_1000"
center_node = "Center_node_J7"
rescue_node = "Rescue_node_J215"
# exercise 1 b)
df_pressure = load_data("data_220208_Grundlagen_der_Digitalisierung.hdf5", "/".join([radius, center_node, rescue_node]),
                        "pressure")
df_demand = load_data("data_220208_Grundlagen_der_Digitalisierung.hdf5", "/".join([radius, center_node, rescue_node]),
                      "demand")
df_req_demand = load_data("data_220208_Grundlagen_der_Digitalisierung.hdf5",
                          "/".join([radius, center_node, rescue_node]), "req_demand")

# exercise 1 c) Check the plausibility
center_node_raw = center_node.replace("Center_node_", "")
check_plausibility(df_req_demand, center_node_raw)

# exercise 2 a)
df_fullfillment = calc_fulfillment_of_demand(df_demand=df_demand, df_req_demand=df_req_demand)

# exercise 2 b)
df_fullfillment = calc_mean_and_std_of_fullfillment(df_fullfillment)


# execerise 2 c)
df_pressure_infos = calc_average_pressure(df_pressure,five_node_tuple(center_node_raw, 'J511', 'J414', 'J417', 'J310') )

# exercise 3 a)
plot_fullfillment(df_fullfillment)




