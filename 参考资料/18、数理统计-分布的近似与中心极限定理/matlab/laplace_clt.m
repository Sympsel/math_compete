function pValue = laplace_clt(k, n, p)
    % de_moivre_laplace_cdf - 利用德莫弗—拉普拉斯中心极限定理近似计算二项分布的累积分布函数
    %
    % 输入参数：
    %   k - X 的上界
    %   n - 试验次数
    %   p - 每次成功的概率，0 < p < 1
    %
    % 输出：
    %   pValue - 近似的 P(X ≤ k)

    % 检查输入参数的有效性
    if p <= 0 || p >= 1
        error('p 必须在 (0, 1) 之间');
    end
    if n < 1
        error('n 必须 ≥ 1');
    end
    
    % 计算均值和标准差
    mu = n * p;
    sigma = sqrt(n * p * (1 - p));
    
    % 连续性校正
    z = (k + 0.5 - mu) / sigma;
    
    % 使用 MATLAB 的 normcdf 函数计算标准正态分布的 CDF
    pValue = normcdf(z, 0, 1); % 计算 z 值的累积分布函数
end
