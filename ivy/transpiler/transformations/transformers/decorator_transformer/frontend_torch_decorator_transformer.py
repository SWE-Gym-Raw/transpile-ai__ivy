# global

# local
from transpiler.transformations.configurations.base_transformer_config import (
    BaseTransformerConfig,
)
from transpiler.transformations.transformer import Transformer
from transpiler.transformations.transformers.decorator_transformer.base_transformer import (
    BaseDecoratorRemover,
)
import transpiler.transformations.transformer_globals as glob


class FrontendTorchDecoratorRemover(BaseDecoratorRemover):
    """
    A subclass to remove certain frontend torch decorators from a given function.
    """

    def __init__(
        self,
        root,
        transformer: Transformer,
        configuration: BaseTransformerConfig,
    ):
        self.root = root
        self.transformer = transformer
        self.configuration = configuration
        self.disallowed_decorators = set(glob.ALL_IVY_FRONTEND_DECORATORS)
