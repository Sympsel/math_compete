function validate_norm(sigma)
%VALIDATE_NORM_PARAM 检查正态分布的标准差是否合法

    if ~isscalar(sigma) || sigma <= 0
        error('标准差 sigma 必须为正数标量');
    end
end
