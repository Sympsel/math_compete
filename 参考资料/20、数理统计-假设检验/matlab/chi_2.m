function [chi2, df, p, reject] = chi2_test(table, alpha)
    % 卡方独立性检验
    % 
    % Parameters
    % ----------
    % table : matrix
    %     任意r×c观测频数表（二维数组）。
    % alpha : float, optional
    %     显著性水平，默认为0.05。
    %
    % Returns
    % -------
    % chi2 : float
    %     卡方统计量。
    % df : int
    %     自由度（(行数-1)*(列数-1)）。
    % p : float
    %     p值（右尾概率）。
    % reject : bool
    %     是否拒绝独立性假设。

    if nargin < 2
        alpha = 0.05; % 默认显著性水平
    end
    
    % 行数和列数
    [rows, cols] = size(table);
    
    % 计算每一行的合计
    row_totals = sum(table, 2);
    
    % 计算每一列的合计
    col_totals = sum(table, 1);
    
    % 所有元素之和（总样本量）
    total = sum(row_totals);
    
    % 计算每个单元格的理论频数 E_ij
    expected = zeros(rows, cols);
    for i = 1:rows
        for j = 1:cols
            expected(i, j) = row_totals(i) * col_totals(j) / total;
        end
    end
    
    % 计算卡方统计量
    chi2 = 0.0;
    for i = 1:rows
        for j = 1:cols
            if expected(i, j) > 0
                chi2 = chi2 + (table(i, j) - expected(i, j))^2 / expected(i, j);
            end
        end
    end
    
    % 计算自由度
    df = (rows - 1) * (cols - 1);
    
    % 正态分布近似计算p值
    if df > 0
        % Z分数 = (卡方统计量 - 自由度) / sqrt(2*自由度)
        z = (chi2 - df) / sqrt(2 * df);
        % p值为右尾概率 = 1 - 左侧累计概率
        p = 1 - normal_cdf(z);
    else
        % 如果自由度为0，p值直接设为1
        p = 1.0;
    end
    
    % 比较p值与显著性水平，判断是否拒绝独立性假设
    reject = p < alpha;
end

function p = normal_cdf(z)
    % 计算标准正态分布的左侧累计概率
    p = 0.5 * (1 + erf(z / sqrt(2)));
end

% ==========================
% 使用示例
% ==========================
% 你的2x2列联表数据
table = [
    10, 40;
    30, 20
];
% 执行卡方独立性检验
[chi2, df, p, reject] = chi2_test(table, 0.05);
% 输出统计量、自由度、p值和结论
fprintf('卡方统计量 = %.4f\n', chi2);
fprintf('自由度 = %d\n', df);
fprintf('p值 = %.4f\n', p);

% 使用if语句输出结论
if reject
    fprintf('结论：拒绝独立性假设\n');
else
    fprintf('结论：不拒绝独立性假设\n');
end
