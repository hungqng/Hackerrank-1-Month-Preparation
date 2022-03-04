function flippingMatrix(matrix){
    let n = matrix.length / 2;
    let max = 0;
    let total = 0;

    for (let r = 0; r < n; r++){
        for (let c = 0; c < n; c++){
            max = Number.MIN_VALUE;
            max = Math.max(matrix[r][c], max);
            max = Math.max(matrix[r][2*n-c-1], max);
            max = Math.max(matrix[2*n-r-1][c], max);
            max = Math.max(matrix[2*n-r-1][2*n-c-1], max);
            total += max;
        }
    }
    return total;
}