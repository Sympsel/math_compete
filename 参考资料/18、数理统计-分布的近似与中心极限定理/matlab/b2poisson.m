function b2poisson(n, p)
    % b2poisson - 二项分布的泊松近似
    % 
    % 输入参数：
    %   n - 二项分布的参数n，即抽样次数
    %   p - 二项分布的参数p，即成功率
    %

    % lambda = np
    lambdaValue = n * p;
    binom(n, p)
    poisson(lambdaValue)
end