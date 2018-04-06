import pandas as pd

csv_path = 'ds_team_project1/data/indices/benchmark_LA/la_benchmark_ds_indices.csv'
o_df = pd.read_csv(csv_path)
new_all_df = o_df[['city', 'restaurant_price_index', 'cpi_index', 'rent_index', 'groceries_index']]

city_list = new_all_df['city'].tolist()


def ds(num):
    csv = city_list[num] + '_ds_labnch_indices.csv'
    csv_path = 'ds_team_project1/data/indices/benchmark_LA/nearby_cities/' + csv
    city_df = pd.read_csv(csv_path)
    new_df = city_df[['city', 'cpi_index', 'rent_index', 'groceries_index', 'restaurant_price_index']]
    new_df['cpi_single_usd'] = new_df['cpi_index'] / 100 * 1760.35
    new_df['cpi_family_usd'] = new_df['cpi_index'] / 100 * 4791.38
    new_df['rent_single_usd'] = new_df['rent_index'] / 100 * (2075.33 + 1582.08) / 2
    new_df['rent_family_usd'] = new_df['rent_index'] / 100 * (3466.02 + 2722.98) / 2
    new_df['groceries_single_usd'] = new_df['groceries_index'] / 100 * 241.80
    new_df['groceries_family_usd'] = new_df['groceries_index'] / 100 * 1209.02
    new_df['restaurant_single_usd'] = new_df['restaurant_price_index'] / 100 * 667.70
    new_df['restaurant_family_usd'] = new_df['restaurant_price_index'] / 100 * 1877.15
    new_list = new_df.mean().tolist()
    df = pd.DataFrame({'city': city_list[num],
                       'cpi_index': new_list[0],
                       'rent_index': new_list[1],
                       'groceries_index': new_list[2],
                       'restaurant_price_index': new_list[3],
                       'cpi_single_usd': new_list[4],
                       'cpi_family_usd': new_list[5],
                       'rent_single_usd': new_list[6],
                       'rent_family_usd': new_list[7],
                       'groceries_single_usd': new_list[8],
                       'groceries_family_usd': new_list[9],
                       'restaurant_single_usd': new_list[10],
                       'restaurant_family_usd': new_list[11], }, index=[num])
    df = df[['city', 'cpi_index', 'rent_index', 'groceries_index', 'restaurant_price_index',
             'cpi_single_usd', 'cpi_family_usd', 'rent_single_usd', 'rent_family_usd', 'groceries_single_usd',
             'groceries_family_usd', 'restaurant_single_usd', 'restaurant_family_usd']]

    return df


# use LA as a benchmark
cols = ['city', 'cpi_index', 'rent_index', 'groceries_index', 'restaurant_price_index',
        'cpi_single_usd', 'cpi_family_usd', 'rent_single_usd', 'rent_family_usd', 'groceries_single_usd',
        'groceries_family_usd', 'restaurant_single_usd', 'restaurant_family_usd']


data = []
for x in range(42):
    data.append(ds(x).values.tolist()[0])


c_df = pd.DataFrame(data, columns=cols)


csv_path = 'ds_team_project1/data/salary/payscale_ds_salary.csv'
salary_df = pd.read_csv(csv_path)

c_df['occupation'] = salary_df['occupation']
c_df['salary_usd'] = salary_df['base_salary_md_pay']
c_df['col_single_usd'] = c_df['cpi_single_usd'] + c_df['rent_single_usd']
c_df['col_family_usd'] = c_df['cpi_family_usd'] + c_df['rent_family_usd']
c_df['ds_single_usd'] = salary_df['base_salary_md_pay'] / 12 - c_df['col_single_usd']
c_df['ds_family_usd'] = salary_df['base_salary_md_pay'] / 12 - c_df['col_family_usd']


c_df['state'] = o_df['state']

new_c_df = c_df[['occupation', 'state', 'city', 'salary_usd', 'cpi_index', 'rent_index', 'groceries_index',
                 'restaurant_price_index', 'cpi_single_usd', 'cpi_family_usd', 'rent_single_usd', 'rent_family_usd',
                 'groceries_single_usd', 'groceries_family_usd', 'restaurant_single_usd', 'restaurant_family_usd',
                 'col_single_usd', 'col_family_usd', 'ds_single_usd', 'ds_family_usd']]


top10_df = new_c_df.nlargest(10, 'salary_usd')


new_c_df.to_csv('ds_team_project1/data/indices/benchmark_LA/monetary_conversion/converted_data_labnch.csv')
top10_df.to_csv('ds_team_project1/data/indices/benchmark_LA/monetary_conversion/top10_data_labnch_salary.csv')


top10_ds_single_df = new_c_df.nlargest(10, 'ds_single_usd')
top10_ds_single_df = top10_ds_single_df[['occupation', 'state', 'city', 'ds_single_usd', 'salary_usd', 'cpi_index', 'rent_index',
                                         'groceries_index', 'restaurant_price_index', 'cpi_single_usd', 'cpi_family_usd',
                                         'rent_single_usd', 'rent_family_usd', 'groceries_single_usd',
                                         'groceries_family_usd', 'restaurant_single_usd', 'restaurant_family_usd',
                                         'col_single_usd', 'col_family_usd', 'ds_family_usd']]


top10_ds_single_df.to_csv('ds_team_project1/data/indices/benchmark_LA/monetary_conversion/top10_data_labnch_ds_single.csv')


top10_ds_family_df = new_c_df.nlargest(10, 'ds_family_usd')
top10_ds_family_df = top10_ds_family_df[['occupation', 'state', 'city', 'ds_family_usd', 'salary_usd', 'cpi_index',
                                         'rent_index', 'groceries_index', 'restaurant_price_index', 'cpi_single_usd',
                                         'cpi_family_usd', 'rent_single_usd', 'rent_family_usd', 'groceries_single_usd',
                                         'groceries_family_usd', 'restaurant_single_usd', 'restaurant_family_usd',
                                         'col_single_usd', 'col_family_usd', 'ds_single_usd']]


top10_ds_family_df.to_csv('ds_team_project1/data/indices/benchmark_LA/monetary_conversion/top10_data_labnch_ds_family.csv')
