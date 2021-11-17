import pyreportjasper

config = {
    'driver': 'csv',
    'data_file': 'fake_data.csv',
    'csv_charset': 'utf-8',
    'csv_out_charset': 'utf-8',
    'csv_field_del': ';',
    'csv_first_row': False,
    'csv_record_del': "\r\n",
    'csv_columns': [
        'person_code',
        'person_name',
        'person_phone',
        'JAN',
        'FEV',
        'MAR',
        'ABR',
        'MAI',
        'JUN',
        'JUL',
        'AGO',
        'SET',
        'OUT',
        'NOV',
        'DEZ',
        'EXT'
    ]
}

if __name__ == '__main__':
    report = pyreportjasper.PyReportJasper()
    report.config('dizimistas.jasper',
                    'envelopes_with_jasper.pdf',
                    output_formats=['pdf'],
                    db_connection=config)
    report.process_report()
