
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Masoud",
    user="postgres",
    password="password",
    port="5432"
    )

# Check Connection to Postgresql database
cursor = conn.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")

drop_tables = '''DROP TABLE IF EXISTS vibexpert_bode_plot; 
                        DROP TABLE IF EXISTS vibexpert_cascade_plot;
                        DROP TABLE IF EXISTS vibexpert_fft_plot;
                        DROP TABLE IF EXISTS vibexpert_psm_plot;     
                        DROP TABLE IF EXISTS vibexpert_orbit_plot;
                        DROP TABLE IF EXISTS vibexpert_order_tracking_plot;
                        DROP TABLE IF EXISTS vibexpert_raw_data_plot;
                        DROP TABLE IF EXISTS vibexpert_rms_peak_plot;
                        DROP TABLE IF EXISTS vibexpert_shaft_centerline_plot;
                        DROP TABLE IF EXISTS vibexpert_timebased_plot; '''
                        
cursor.execute(drop_tables)
conn.commit()
print("Table dropped successfully in PostgreSQL ")
