from utils import load_data, filter_sort, formatted_data


def main():
    data = load_data()
    data = filter_sort(data)

    for i in range(5):
        print(formatted_data(data[i]))


if __name__ == '__main__':
    main()
