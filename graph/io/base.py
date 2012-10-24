from abc import ABCMeta, abstractmethod

from io import StringIO


class GraphSerializer(metaclass=ABCMeta):

    @abstractmethod
    def iter_serialize(self, graph):
        """Serialize a graph, yielding parts of the result when available."""

    def serialize(self, graph, stream):
        """Serialize a graph to a writable stream.

        If *stream* is a string it is interpreted as a filepath.  The contents
        of the file will be replaced by the graphs representation.  If *stream*
        is a file-like object the user is responsible for opening and closing
        the stream.
        """
        def inner_serialize(graph, stream):
            for partial in self.iter_serialize(graph):
                stream.write(partial)

        if isinstance(stream, str):
            with open(stream, mode="wt") as outfile:
                inner_serialize(graph, outfile)
        else:
            inner_serialize(graph, stream)

    def serialize_string(self, graph):
        """Serialize a graph to a string."""
        return "".join(self.iter_serialize(graph))


class GraphDeserializer(metaclass=ABCMeta):

    @abstractmethod
    def iter_deserialize(self, iterable, cls):
        """Decode a graph from an iterable of strings."""

    def deserialize(self, stream, cls):
        """Decode a graph from a readable stream.

        If *stream* is a string it is interpreted as a filepath.  If *stream*
        is a file-like object the user is responsible for opening and closing
        the stream.
        """
        if isinstance(stream, str):
            with open(stream, mode="rt") as infile:
                return self.iter_deserialize(infile, cls)
        else:
            return self.iter_deserialize(stream, cls)

    def decode_string(self, string, cls):
        """Decode a graph from a string."""
        return self.iter_deserialize(StringIO(string), cls)
