
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Masoud",
    user="postgres",
    password="Password",
    port="5432"
    )
cursor = conn.cursor()
# Print PostgreSQL Connection properties
print ( conn.get_dsn_parameters(),"\n")
# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")


create_table_query = '''DROP TABLE IF EXISTS vibexpert_bode_plot
                              ; 
                        DROP TABLE IF EXISTS vibexpert_cascade_plot
                              ;
                        DROP TABLE IF EXISTS vibexpert_fft_plot
                              ;
                        DROP TABLE IF EXISTS vibexpert_psm_plot
                             ;     
                        DROP TABLE IF EXISTS vibexpert_orbit_plot
                              ;
                        DROP TABLE IF EXISTS vibexpert_order_tracking_plot
                            ;
                        DROP TABLE IF EXISTS vibexpert_raw_data_plot
                              ;
                        DROP TABLE IF EXISTS vibexpert_rms_peak_plot
                              ;
                        DROP TABLE IF EXISTS vibexpert_shaft_centerline_plot
                              ;
                        DROP TABLE IF EXISTS vibexpert_timebased_plot
                              ;                               
                              '''
cursor.execute(create_table_query)
conn.commit()
print("Table created successfully in PostgreSQL ")
