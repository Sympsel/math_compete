function validate_gamma_param(k, lambda)
%VALIDATE_GAMMA_PARAM 检查伽马分布参数合法性

    if ~isscalar(k) || ~isscalar(lambda) || k <= 0 || lambda <= 0
        error('形状参数 k 和速率参数 lambda 都必须为正标量');
    end
end
