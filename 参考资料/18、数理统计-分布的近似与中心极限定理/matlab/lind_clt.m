function pValue = lind_clt(x, mu, var, n)
    % lindeberg_levy_cdf - 利用林德伯格–莱维中心极限定理近似计算 P(S_n ≤ x)
    %
    % 输入参数：
    %   x - S_n 的上界
    %   mu - 每个 X_i 的均值
    %   var - 每个 X_i 的方差，必须 ≥ 0
    %   n - 独立同分布随机变量的个数，n ≥ 1
    %
    % 输出：
    %   pValue - 近似的 P(S_n ≤ x)

    % 检查输入参数的有效性
    if var < 0
        error('var 必须非负');
    end
    if n < 1
        error('n 必须 ≥ 1');
    end
    
    % 计算标准差
    sigma_n = sqrt(n * var);
    
    % 计算标准化的 z 值
    z = (x - n * mu) / sigma_n;
    
    % 使用 MATLAB 的 normcdf 函数计算标准正态分布的 CDF
    pValue = normcdf(z, 0, 1); % 计算 z 值的累积分布函数
end
