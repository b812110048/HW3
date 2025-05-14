def quick_sort(arr, depth=0):
    indent = "  " * depth  # 用來讓輸出看起來有層次
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    # 分割資料
    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    # 印出目前的排序狀態
    print(f"{indent}Pivot: {pivot}")
    print(f"{indent}Left: {left}")
    print(f"{indent}Right: {right}")
    print()

    # 遞迴排序左右兩邊
    return quick_sort(left, depth + 1) + [pivot] + quick_sort(right, depth + 1)


if __name__ == "__main__":
    demo = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
    print("原始陣列：")
    print(demo)
    print("\n排序過程：\n")
    sorted_demo = quick_sort(demo)
    print("\n排序後結果：")
    print(sorted_demo)
