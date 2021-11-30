
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Masoud",
    user="postgres",
    password="password",
    port="5432"
    )
cursor = conn.cursor()
# Print PostgreSQL Connection properties
print ( conn.get_dsn_parameters(),"\n")
# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")


create_table_query = '''CREATE TABLE IF NOT EXISTS vibexpert_bode_plot
                              (date date,
                               time varchar(1000),
                               kks varchar(1000) , 
                               description varchar(1000),
                               unit_magnitude varchar(1000),
                               unit_phase varchar(1000),
                               orders json,
                               rpm  json,
                               size_order_1  integer,
                               magnitude_order_1 json,
                               phase_order_1 json,
                               size_order_2  integer,
                               magnitude_order_2 json,
                               phase_order_2 json,
                               size_order_3  integer,
                               magnitude_order_3 json,
                               phase_order_3 json,
                               size_order_4  integer,
                               magnitude_order_4 json,
                               phase_order_4 json
                               ); 
                         CREATE TABLE IF NOT EXISTS vibexpert_cascade_plot
                              (date date,
                               time varchar(1000),
                               kks varchar(1000), 
                               description varchar(1000),
                               unit varchar(1000),
                               plot_type varchar(1000),
                               speed_type  varchar(1000),
                               rpm_0  float,
                               drpm float,
                               size_rpm float,
                               frequency_0 float,
                               dfrequency float,
                               size_frequency float,
                               data json);
                        CREATE TABLE IF NOT EXISTS vibexpert_fft_plot
                              (date varchar,
                               time varchar(1000),
                               kks varchar(1000) , 
                               description varchar(1000),
                               unit varchar(1000),
                               fft_values json,
                               f_0  integer,
                               df  integer);
                        CREATE TABLE IF NOT EXISTS vibexpert_psm_plot
                              (date varchar,
                               time varchar(1000),
                               kks varchar(1000) , 
                               description varchar(1000),
                               unit varchar(1000),
                               psm_values json,
                               f_0  integer,
                               df  integer);     
                         CREATE TABLE IF NOT EXISTS vibexpert_orbit_plot
                              (date varchar,
                               kks varchar(1000), 
                               unit varchar(1000),
                               orders json,
                               x_unfiltered  json,
                               y_unfiltered  json,
                               x_filtered1 json,
                               y_filtered1 json,
                               x_filtered2 json,
                               y_filtered2 json,
                               x_filtered3 json,
                               y_filtered3 json,
                               x_filtered4 json,
                               y_filtered4 json,
                               orbit_buffer  integer,
                               description varchar(1000),
                               time varchar(1000)
                               );
                     CREATE TABLE IF NOT EXISTS vibexpert_order_tracking_plot
                              (date date,
                               time varchar(1000),
                               kks varchar(1000) , 
                               description varchar(1000),
                               unit_magnitude varchar(1000),
                               unit_phase varchar,
                               orders json,
                               rpm  json,
                               size_order_1  float,
                               magnitude_order_1 json,
                               phase_order_1 json,
                               size_order_2  float,
                               magnitude_order_2 json,
                               phase_order_2 json,
                               size_order_3  float,
                               magnitude_order_3 json,
                               phase_order_3 json,
                               size_order_4  float,
                               magnitude_order_4 json,
                               phase_order_4 json
                               );
                     CREATE TABLE IF NOT EXISTS vibexpert_raw_data_plot
                              (date date,
                               time varchar(100),
                               kks varchar(100) , 
                               data json);
                     CREATE TABLE IF NOT EXISTS vibexpert_rms_peak_plot
                              (date varchar,
                               time varchar(1000),
                               kks varchar(1000) , 
                               description varchar(1000),
                               unit varchar(1000),
                               size_array  integer,
                               data json);
                     CREATE TABLE IF NOT EXISTS vibexpert_shaft_centerline_plot
                              (date date,
                               time varchar(1000),
                               kks varchar(1000) , 
                               description varchar(1000),
                               unit varchar(1000),
                               size_array  json,
                               probe_x json,
                               probe_y json,
                               reference json);
                         CREATE TABLE IF NOT EXISTS vibexpert_timebased_plot
                              (date varchar(1000),
                               kks varchar(1000), 
                               unit varchar(1000),
                               orders json,
                               x_unfiltered  json,
                               y_unfiltered  json,
                               x_filtered1 json,
                               y_filtered1 json,
                               x_filtered2 json,
                               y_filtered2 json,
                               x_filtered3 json,
                               y_filtered3 json,
                               x_filtered4 json,
                               y_filtered4 json,
                               orbit_buffer  integer,
                               description varchar(1000),
                               time varchar(1000)
                               );                               
                              '''
                        
                              
cursor.execute(create_table_query)
conn.commit()
print("Table created successfully in PostgreSQL ")
